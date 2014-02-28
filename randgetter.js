requestNumList = function() {
    var request = new XMLHttpRequest();
    var URL = "http://localhost:8000/cgi-bin/json_random.py?length=30"

    request.onreadystatechange = function() {
        console.log("in function: " + request.readyState)
        if (request.readyState==4 && request.status==200)
          {
              var A = JSON.parse(request.responseText)
              var mylist = document.getElementById("rlist")              
              for(i=0; i<A.length;i++) {
                  console.log(A[i])
                  var li = document.createElement("li")
                  li.innerHTML = A[i]
                  mylist.appendChild(li)
              }
          }   
    }
    request.open("GET",URL,true);
    request.send();
}