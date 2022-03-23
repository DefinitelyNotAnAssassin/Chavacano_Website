const form = document.getElementById("text")
const translated = document.getElementById("password")


let socket = io()



form.addEventListener("input", function(){
  socket.emit("receiver", {
    msg: form.value,
  })
  

  
})

socket.on("translate", function(text){
  
  translatedval = JSON.stringify(text)
  translated.value = text
  
})