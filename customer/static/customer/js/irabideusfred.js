function validateInputText(fieldValue,id){
  var letters = /^[a-zA-Z]+$/;
  if(fieldValue.value.match(letters)){

  }else{
    document.getElementById(id).style.display = "block";
  }

}
