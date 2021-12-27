document.getElementById("check").addEventListener("click",async function(){
  var pw = {}
  var randID = Math.round(Math.random()*1000000)
  pw[randID] = document.getElementById("pwrd").value
  var badlist = await (await fetch("https://raw.githubusercontent.com/iam-py-test/password-check/main/data/worst_password.txt")).text().split("\n")
  if(badlist.includes(pw[randID])){
    document.getElementById("isinbad").textContent = "Your password is in the list of worst passwords"
  }
  else{
    document.getElementById("isinbad").textContent = "Your password is not in the list of worst passwords"
  }
  pw[randID] = null
  delete pw[randID]
  pw = {}
  randID = 0
})

