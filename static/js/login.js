window.onload = function(){


let authStatusElem = document.getElementById("loginmsg").innerHTML = '<h5>Делаем запрос к API...</h5>';


$.ajax({ url: "api/auth", 	
method: "POST", 
data: {"idt": 1}, 	
success: function(data) { 	
console.log(data);

if (data == 'success'){
	let authStatusElem1 = document.getElementById("loginmsg").innerHTML = ' <select class="bootstrap-select"> <option value="-1" selected disabled name="sex">Выбирите департамент</option> <option value="police">Полицейский департамент</option>';
	$("#ETHER").css("color", "var(--cadsuccess)");
	//window.location.replace("http://localhost:9999/dashboard");

} else{
	let authStatusElem2 = document.getElementById('loginmsg').innerHTML = '<h5 class="text-danger">У вас нету доступа к базе данных</h5>'
	authStatusElem2.stop();
	authStatusElem2.classList.remove('blink-animation');

}

} 
}); 

}