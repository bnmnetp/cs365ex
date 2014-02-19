/* This is a comment */

hello = function() {
    var newh1 = document.createElement('h1')
    newh1.innerHTML = 'Hello World!'
    document.getElementById("temp1").appendChild(newh1)
    //document.body.appendChild(newh1)
}
// this is a single line comment
window.onload = hello
