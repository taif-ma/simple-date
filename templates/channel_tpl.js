
$( document ).ready(() => {
    //console.log('ready!');
    let token = '{{ user.profile.get_token }}';
    // alert(token);
    let socket  =  new WebSocket("ws://localhost:8080/online/");
    console.log('asdfasdsafa');
        let data = {
            action: 'login', 
            data: {
                token: token,
                userAgent: window.navigator.userAgent
            }
        }
    //console.log(data)
    //socket.send(JSON.stringify(data));
    socket.onopen = function () {
        socket.send(JSON.stringify(data)); 
        
    };
    
});
