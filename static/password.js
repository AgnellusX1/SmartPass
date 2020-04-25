$(document).ready(function () {
var resultnew = document.getElementById('generic')
var password=document.getElementById('password')
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

        var val=password.value
        var generic_result=zxcvbn(val)
        var strength = {
              0: "Weakest",
              1: "Weak",
              2: "OK",
              3: "Good",
              4: "Strong"
            }

          if (val!==""){
            resultnew.innerHTML = strength[generic_result.score];
        }
        else{
            resultnew.innerHTML = "";
        }

        if(document.getElementById("username").value == document.getElementById("password").value){
                alert("Warning: Do Not Use Username as Password")
                }
    });

});