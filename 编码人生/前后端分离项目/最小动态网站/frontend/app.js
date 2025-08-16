const apiUrl="http://localhost:3000/api/users";

async function fetchUsers(){

	const res= await fetch(apiUrl);
	
