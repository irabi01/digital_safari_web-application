$(document).ready(function(){

  var dateToday = new Date();
  var dates = $("#departure, #return").datepicker({
      defaultDate: "+1w",
      changeMonth: true,
      numberOfMonths: 3,
      minDate: dateToday,
      onSelect: function(selectedDate) {
          var option = this.id == "departure" ? "minDate" : "maxDate",
              instance = $(this).data("datepicker"),
              date = $.datepicker.parseDate(instance.settings.dateFormat || $.datepicker._defaults.dateFormat, selectedDate, instance.settings);
          dates.not(this).datepicker("option", option, date);
      }
  });
//=========================== loading script===========================
  $(".preload").fadeOut(3000, function(){
    $(".available_content").fadeIn(1000);
    $(".error_page_container").fadeIn(1000);
  });

//===================== passenger details script==============================
  $("#Radio_passenger").click(function(){
    $(".peronal_address").slideDown();
    $(".save_passenger_info").show();
    $("#Radio_passenger").hide();
    $(".form-check-label").hide();
  });

  $(function () {
    $('[data-toggle="tooltip"]').tooltip()
  });

  // var mysearch = document.getElementById('below_twenty');
  // var kati_ya_twenty_to_thirty = document.getElementById('kati_ya_twenty_to_thirty');
  //
  // mysearch.addEventListener('mouseover', function() {
  //   document.getElementById('for_searching_data').value = '22000';
  // });
  //
  // kati_ya_twenty_to_thirty.addEventListener('mouseover', function() {
  //   document.getElementById('for_searching_data').value = 'kati_ya_twenty_to_thirty';
  // });



  // $("#success_message").fadeOut(3000);

  // $(function() {
  //   $('#spoint').keyup(function(){
  //     // alert("hello irabi coder");
  //     $.ajax({
  //       type: "POST",
  //       url: "{% url 'search_route' %}",
  //       data: {
  //         'startingpoint_variable' : $('#spoint').val(),
  //         'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
  //       },
  //       success:searchSuccess,
  //       dataType: 'html'
  //     });
  //   });
  // });

  // function randomString() {
  // 	var chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXTZabcdefghiklmnopqrstuvwxyz";
  // 	var string_length = 8;
  // 	var randomstring = '';
  // 	for (var i=0; i<string_length; i++) {
  // 		var rnum = Math.floor(Math.random() * chars.length);
  // 		randomstring += chars.substring(rnum,rnum+1);
  // 	}
  // 	// document.randform.randomfield.value = randomstring;
  //   document.getElementById('secrete_code').value = randomstring;
  // }
var boardingpoints;
var dropingpoints;
function boardDropEvaluate(){
  var origin = document.getElementById('from_point_orign').value;
  var destination = document.getElementById('to_point_destination').value;
  if(origin =="Dodoma" && destination == "Dar es salaam"){
    boardingpoints = "<option selected hidden>Board point</option><option value='Jamatini'>Jamatini</option><option value='Nanenane'>Nanenane</option><option value='Gairo'>Gairo</option><option value='Area C'>Area C</option>";
    dropingpoints = "<option selected hidden>Drop points</option><option value='Kibaha'>Kibaha</option><option value='Mbezi'>Mbezi</option><option value='Ubungo'>Ubungo</option>";
  }else if(origin =="Dar es salaam" && destination == "Dodoma"){
    dropingpoints = "<option selected hidden>Board point</option><option value='Jamatini'>Jamatini</option><option value='Nanenane'>Nanenane</option><option value='Gairo'>Gairo</option><option value='Area C'>Area C</option>";
    boardingpoints = "<option selected hidden>Drop points</option><option value='Kibaha'>Kibaha</option><option value='Mbezi'>Mbezi</option><option value='Ubungo'>Ubungo</option>";
  }
}
function createHandler(counter){
  return function(){
    eval("avalue"+counter+"=document.getElementById(counter).innerHTML");
    if(eval("seatno"+counter) != eval("avalue"+counter) && selectCount<6){
      eval("seatno"+counter +"="+ counter);
      selectCount ++;
      document.getElementById('totalCountSeat').innerHTML = selectCount;
      var newDiv = document.createElement('div');
      newDiv.className = 'w3-card-4 w3-black w3-text-white added_seat';
      newDiv.style.width = '20%';
      newDiv.style.textAlign = 'center';
      newDiv.style.margin = '2px';
      newDiv.style.float = 'left';
      newDiv.style.fontSize = '12px';
      newDiv.style.borderRadius = '10px';
      newDiv.appendChild(document.createTextNode(eval("avalue"+counter)));
      get_seat_value.style.color = '#000';
      get_seat_value.appendChild(newDiv);
      eval("a"+counter).style.backgroundColor = '#001f01';
      eval("a"+counter).style.color = '#fff';
      eval("a"+counter).style.borderRadius = '100%';
      var set_nauli = document.getElementById('fare_part');
      set_nauli.innerHTML = bus_nauli *selectCount;
      document.getElementById('modelFarePart').innerHTML = bus_nauli *selectCount;
      document.getElementById('totalseatsInputFields').value = selectCount;
      document.getElementById('amount_total').value = bus_nauli *selectCount;
      if(selectCount < 1){
        document.getElementById('proceed_button').style.display = 'none';
      }
      else {
        document.getElementById('proceed_button').style.display = 'block';
      }

      // Generate random number for ticket_number
      var chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXTZabcdefghiklmnopqrstuvwxyz";
      var string_length = 15;
      var randomstringTicket = '';
      for (var i=0; i<string_length; i++) {
        var rnum = Math.floor(Math.random() * chars.length);
        randomstringTicket += chars.substring(rnum,rnum+1);
      }

      boardDropEvaluate();
      document.getElementById('formDetails').innerHTML += "<div id='form"+counter+"'style='border:1px solid #0654a2;padding:0px 20px; margin-bottom:10px'><div class='row row_ya_seat_number'><div class='col-md-12'><h5 style='color:black'>Seat No. "+counter+"</h5></div></div><div class='row'><div class='col-md-6'><div class='form-group'><input type='hidden' name='seatnumber' value='"+counter+"' class='w3-input' placeholder='Seat number' required></div></div><div class='col-md-6'><div class='form-group'><input type='hidden' name='nauli' value='"+bus_nauli+"' class='w3-input' placeholder='Bus Fare' required></div></div></div><div class='row'><div class='col-md-6'><div class='form-group'><input type='text' id='' name='firstname'  placeholder='First Name' class='w3-input' required/></div></div> <div class='col-md-6'><div class='form-group'><input type='text' id='' name='lastname' placeholder='Last Name' class='w3-input' required/></div></div></div><div class='row'><div class='col-md-6'><div class='form-group'><input type='hidden' name ='secretecode' id='secretecode"+selectCount+"' value='"+randomstring+"' class='w3-input'></div></div><div class='col-md-6'><div class='form-group'><input type='hidden' name ='ticket_number' id='ticket_number' value='"+randomstringTicket+"' class='w3-input'></div></div></div><div class='row'><div class='col-md-6'><div class='form-group'><input type='text' name='boardingpoint' value='' class='w3-input' placeholder='Bording Point' list='boarding_point' required><datalist id='boarding_point'>"+boardingpoints+"</datalist></div></div><div class='col-md-6'><div class='form-group'><input type='text' name='dropingpoint' value='' class='w3-input' placeholder='Droping Point' list='droping_point' required><datalist id='droping_point'>"+dropingpoints+"</datalist></div></div></div><div></div></div>"
      }
    };
}
var selectCount;
function searchSuccess(data, textStatus, jqXHR){
  $('#search_results').html(data);
}
var get_seat_value = document.getElementById('number-of-seats');
var availableSeat = document.getElementById('center_column_available_bus');
var nauli = document.getElementById('fare_part').innerHTML;
var nauli_to_int = parseInt(nauli);
document.getElementById('fare_part').innerHTML = 0;
document.getElementById('fare_part').style.display = "inline-block";
var total_nauli;
var bus_nauli;
var counter = 1;
while(counter <= 49){
  bus_nauli =0+ nauli_to_int;

 selectCount=0;
  eval("seatno"+counter+"=0");// ninu
  eval("a"+ counter +"= document.getElementById(counter)");
  eval("a"+ counter).addEventListener('click', createHandler(counter));
  counter++;
}
document.getElementById('formDetails').innerHTML +="";



// remove child element from the parent node.
get_seat_value.addEventListener('click', removeDivSeat);

// function removeDivSeat(e){//sasa mimi nataka kupitisha div "id" ya div ninayofuta....
//   if (e.target.classList.contains('added_seat')) {
//     if (confirm('Are you sure want to remove this seat?')) {
//       var deleteDiv = e.target.parentElement;
//       // var deleteDiv = document.getElementsByTagName('div');
//       console.log(deleteDiv);
//       get_seat_value.removeChild(deleteDiv);
//     }
//   }
// }

function removeDivSeat(e){
  console.log('clicked');// tunangalia kilichobonyezwa
  if (e.target.classList.contains('added_seat')) {
        console.log(e.target.classList.contains('added_seat'));
        if (confirm('Are you sure you want to delete this seat?')) {
              console.log('yes');
              //create variable ya kupokea ile child node.
              var seat_div = e.target;
              console.log(seat_div);
              get_seat_value.removeChild(seat_div);
              var seatno = seat_div.innerHTML;
              eval("a"+seatno).style.backgroundColor = '';
              eval("a"+seatno).style.color = '';
              eval("a"+seatno).style.borderRadius = '';
              selectCount--;
              document.getElementById('form'+seatno).remove();
              var set_nauli = document.getElementById('fare_part');
              set_nauli.innerHTML = bus_nauli* selectCount;
              document.getElementById('modelFarePart').innerHTML = bus_nauli *selectCount;
              document.getElementById('totalseatsInputFields').value = selectCount;
              document.getElementById('totalCountSeat').innerHTML = selectCount;
              document.getElementById('amount_total').value = bus_nauli *selectCount;

              if(selectCount < 1){
                document.getElementById('proceed_button').style.display = 'none';
              }
              else {
                document.getElementById('proceed_button').style.display = 'block';
              }
              eval("seatno"+seatno +"=''");
        }
  }
}


// function filterFare(e){
//   var text = e.target.value.toLowerCase();
//   var fareList = availableSeat.getElementsByTagName('div');
//   Array.from(fareList).foreEach(function(item){
//     var farelistName = item.firstChild.textContent;
//     console.log(farelistName);
//   })
//   // console.log(getElementById('center_column_available_bus'));
// }




});
