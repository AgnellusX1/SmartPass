$(document).ready(function () {
    $('#password').keyup(function (event) {
        $.ajax({
            data:{ password:$('#password').val() },
        type : 'POST',
        url : '/'
        }).done(function(data){
            if(data.pw){
                $('#result').text(data.pw).show();
                return data.pw
            }

        });


        event.preventDefault();

        if(document.getElementById("username").value == document.getElementById("password").value){
                alert("Warning: Do Not Use Username as Password")
                }
    });
});