function updateGamezone(){
    var gamezoneInput = document.getElementById("gamezone_input")
    
    $.ajax({
        url: "/api/gamezone",
        method: "POST",
        data: {gamezone: gamezoneInput.value},
        success: function(data){
            console.log(data)
            if (data == 'success'){
                Notiflix.Notify.Success('Зона успешно обновлена')
            } else {
                Notiflix.Notify.Failure('Возникла ошибка с обновлением зоны')
            }
        }
    });
}