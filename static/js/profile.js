function updateName(){
    var updateInput = document.getElementById("profile-name")
    
    $.ajax({
        url: "/api/name/update",
        method: "POST",
        data: {gamezone: updateInput.value},
        success: function(data){
            console.log(data)
            if (data == 'success'){
                Notiflix.Notify.Success('Имя успешно обновлено')
            } else {
                Notiflix.Notify.Failure('Возникла ошибка с обновлением имени')
            }
        }
    });
}