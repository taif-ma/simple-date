
$( document ).ready(() => {
    console.log('ready!');
    let token = {{ user.profile.get_token }};
    alert(token);
    let connection  =  new WebSocket("ws://localhost:5555/online/");
});