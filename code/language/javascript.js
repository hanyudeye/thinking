// javascript 工具函数大全

// # 数组
// 布尔全等判断，判断每一值 都符合函数条件
const all=(arr,fn=Boolean)=>arr.every(fn)

// console.log(all([4,2,3],x=>x>1)); //True
// console.log(all([4,2,3],x=>x>3)); //False
// console.log(all(["helli","gooo"],x=> typeof x=="string")) // 每个值都是字符串

