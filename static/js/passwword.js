$(document).ready(function () {

    //     $('#uname').keyup(function () {
    //     ('#uname').val();
    // });


    $('#password').keyup(function () {

        $('#result').html(checkStrength($('#password').val(),$('#uname').val()))
        console.log("Test");
    })
    function checkStrength(password,uname) {
        var strength = 0
        console.log('name:' + uname);
        console.log('pass:' + password);

        if (password == uname) {
            $('#result').removeClass()
            $('#result').addClass('short')
            return 'same id pass'
        }

        if (password.length < 6) {
            $('#result').removeClass()
            $('#result').addClass('short')
            return 'Too short'
        }
        if (password.length > 7) strength += 1
        // If password contains both lower and uppercase characters, increase strength value.
        if (password.match(/([a-z].*[A-Z])|([A-Z].*[a-z])/)) strength += 1
        // If it has numbers and characters, increase strength value.
        if (password.match(/([a-zA-Z])/) && password.match(/([0-9])/)) strength += 1
        // If it has one special character, increase strength value.
        if (password.match(/([!,%,&,@,#,$,^,*,?,_,~])/)) strength += 1
        // If it has two special characters, increase strength value.
        if (password.match(/(.*[!,%,&,@,#,$,^,*,?,_,~].*[!,%,&,@,#,$,^,*,?,_,~])/)) strength += 1
        // Calculated strength value, we can return messages
        // If value is less than 2
        if (strength < 2) {
            $('#result').removeClass()
            $('#result').addClass('weak')
            return 'Weak'
        } else if (strength == 2) {
            $('#result').removeClass()
            $('#result').addClass('good')
            return 'Good'
        }

        if (password == uname){
        $('#result').removeClass()
        $('#result').addClass('strong')
        return 'same pass uname'
    }
        else {
            $('#result').removeClass()
            $('#result').addClass('strong')
            return 'Strong'
        }
    }
});

