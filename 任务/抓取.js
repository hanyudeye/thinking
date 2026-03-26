import fs from "fs";
// 追加正文
import {JSDOM} from "jsdom";
import {Readability} from "@mozilla/readability";

const API="https://hacker-news.firebaseio.com/v0";

async function getTop(){
    const ids=await fetch(`${API}/topstories.json`).then(r=>r.json());

    return ids.slice(0,50);
}

async function getItem(id){
    return fetch(`${API}/item/${id}.json`).then(r=>r.json());
}

async function extract(url){
    const html=await fetch(url).then(r=>r.text());
    const dom=new JSDOM(html,{url});
    const reader=new Readability(dom.window.document);
    const article = reader.parse();
    return article.textContent;
}

async function main(){
    const ids=await getTop();
    let md="# Hackernews Daily\n\n";
    for(const id of ids){
        const item=await getItem(id);
        md+=`## ${item.title}\n`;
        md+=`URL:${item.url}\n`;
        md+=`Score:${item.score}\n`;
        let article=await extract(item.url)

        md+=`Article:${article}`;

    }

    fs.writeFileSync("hn.md",md);
}

main();
