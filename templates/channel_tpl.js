
$( document ).ready(() => {
    console.log('ready!');
    let token = '{{ user.profile.get_token }}';
    // alert(token);
    let socket  =  new WebSocket("ws://localhost:5555/online/");
    $('#test-socket').on('click',() => {
        console.log('asdfasdsafa');
        let data = {
            action: 'login', 
            data: {
                token: token,
                userAgent: window.navigator.userAgent
            }
        }
        socket.send(JSON.stringify(data));
    })
});