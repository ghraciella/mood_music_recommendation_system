$(document).ready(function(){
	$('.header').height($(window).height());
})


var ready = (callback) => {
    if (document.readyState != "loading") callback();
    else document.addEventListener("DOMContentLoaded", callback);
}
ready(() => {
    document.querySelector(".header").style.height = window.innerHeight + "px";
})

const showSignUp = () => {
    const form = document.querySelector("#sign-up-form");
    form.style.zIndex = 1000;
    form.hidden = false;

}

const showLogIn = () => {
    const form = document.querySelector("#log-in-form");
    form.style.zIndex = 1000;
    form.hidden = false;

}
