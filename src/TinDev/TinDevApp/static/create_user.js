function Create_New_User(){
	
	first_name = document.getElementById("first").value;
	last_name = document.getElementById("last").value;

	username = document.getElementById("username").value;
	password = document.getElementById("password").value;


	year_of_experience = document.getElementById("years").value;
	zipcode = document.getElementById("zipcode").value;


	skills = document.getElementById("skills").value;


	let data = first_name+' '+last_name+','+username+','+password+','+ String(year_of_experience) + ',' + String(zipcode) + ',' + skills;
  
var a = document.createElement("a");
a.href = window.URL.createObjectURL(new Blob(["CONTENT"], {type: "text/plain"}));
a.download = "demo.txt";
a.click();

	window.open("https://www.w3schools.com");

}
