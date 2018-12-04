$(document).ready(function(){


  var semi_luxury = document.getElementById('semi_luxury');
  var luxury = document.getElementById('luxury');
  var ordinary = document.getElementById('ordinary');
  var _0600am = document.getElementById('_0600am');
  var _0630am = document.getElementById('_0630am');
  var _0700am = document.getElementById('_0700am');
  var _0730am = document.getElementById('_0730am');
  var _0800am = document.getElementById('_0800am');
  var _0830am = document.getElementById('_0830am');
  var _0900am = document.getElementById('_0900am');
  var _0930am = document.getElementById('_0930am');
  var _1000am = document.getElementById('_1000am');
  var _1030am = document.getElementById('_1030am');
  var _1100am = document.getElementById('_1100am');
  var _1130am = document.getElementById('_1130am');
  var _1200pm = document.getElementById('_1200pm');
  var _1230pm = document.getElementById('_1230pm');
  var _1300pm = document.getElementById('_1300pm');
  var _1330pm = document.getElementById('_1330pm');
  var _1400pm = document.getElementById('_1400pm');
  var _1430pm = document.getElementById('_1430pm');
  var _1500pm = document.getElementById('_1500pm');
  var _1530pm = document.getElementById('_1530pm');
  var _1600pm = document.getElementById('_1600pm');
  var _1630pm = document.getElementById('_1630pm');
  var _1700pm = document.getElementById('_1700pm');
  var _1730pm = document.getElementById('_1730pm');
  var _1800pm = document.getElementById('_1800pm');
  var _1830pm = document.getElementById('_1830pm');
  var _1900pm = document.getElementById('_1900pm');
  var _1930pm = document.getElementById('_1930pm');
  var _2000pm = document.getElementById('_2000pm');
  var _2030pm = document.getElementById('_2030pm');


  luxury.addEventListener('mouseover', function(){
    document.getElementById('for_searching_data').value = 'Luxury';
  });
  luxury.addEventListener('click', function() {
    document.forms['route_form'].action = '/digital_safari/available_routes/luxury/';
    document.forms['route_form'].submit();
  });
  //
  semi_luxury.addEventListener('mouseover', function(){
    document.getElementById('for_searching_data').value = 'Semi-Luxury';
  });
  semi_luxury.addEventListener('click', function() {
    document.forms['route_form'].action = '/digital_safari/available_routes/semi_luxury/';
    document.forms['route_form'].submit();
  });

  ordinary.addEventListener('mouseover', function(){
    document.getElementById('for_searching_data').value = 'Ordinary';
  });
  ordinary.addEventListener('click', function() {
    document.forms['route_form'].action = '/digital_safari/available_routes/ordinary_bus/';
    document.forms['route_form'].submit();
  });

_0600am.addEventListener('mouseover', function(){
  document.getElementById('for_searching_data').value = '06:00am';
});
_0600am.addEventListener('click', function() {
  document.forms['route_form'].action = '/digital_safari/available_routes/time_0600_am/';
  document.forms['route_form'].submit();
});

_0630am.addEventListener('mouseover', function(){
  document.getElementById('for_searching_data').value = '06:30am';
});
_0630am.addEventListener('click', function() {
  document.forms['route_form'].action = '/digital_safari/available_routes/time_0630_am/';
  document.forms['route_form'].submit();
});


_0700am.addEventListener('mouseover', function(){
  document.getElementById('for_searching_data').value = '07:00am';
});
_0700am.addEventListener('click', function() {
  document.forms['route_form'].action = '/digital_safari/available_routes/time_0700_am/';
  document.forms['route_form'].submit();
});

_0730am.addEventListener('mouseover', function(){
  document.getElementById('for_searching_data').value = '07:30am';
});
_0730am.addEventListener('click', function() {
  document.forms['route_form'].action = '/digital_safari/available_routes/time_0730_am/';
  document.forms['route_form'].submit();
});

_0800am.addEventListener('mouseover', function(){
  document.getElementById('for_searching_data').value = '08:00am';
});
_0800am.addEventListener('click', function() {
  document.forms['route_form'].action = '/digital_safari/available_routes/time_0800_am/';
  document.forms['route_form'].submit();
});

_0830am.addEventListener('mouseover', function(){
  document.getElementById('for_searching_data').value = '08:30am';
});
_0830am.addEventListener('click', function() {
  document.forms['route_form'].action = '/digital_safari/available_routes/time_0830_am/';
  document.forms['route_form'].submit();
});

_0900am.addEventListener('mouseover', function(){
  document.getElementById('for_searching_data').value = '09:00am';
});
_0900am.addEventListener('click', function() {
  document.forms['route_form'].action = '/digital_safari/available_routes/time_0900_am/';
  document.forms['route_form'].submit();
});

_0930am.addEventListener('mouseover', function(){
  document.getElementById('for_searching_data').value = '09:30am';
});
_0930am.addEventListener('click', function() {
  document.forms['route_form'].action = '/digital_safari/available_routes/time_0930_am/';
  document.forms['route_form'].submit();
});

_1000am.addEventListener('mouseover', function(){
  document.getElementById('for_searching_data').value = '10:00am';
});
_1000am.addEventListener('click', function() {
  document.forms['route_form'].action = '/digital_safari/available_routes/time_1000_am/';
  document.forms['route_form'].submit();
});

_1030am.addEventListener('mouseover', function(){
  document.getElementById('for_searching_data').value = '10:30am';
});
_1030am.addEventListener('click', function() {
  document.forms['route_form'].action = '/digital_safari/available_routes/time_1030_am/';
  document.forms['route_form'].submit();
});


_1100am.addEventListener('mouseover', function(){
  document.getElementById('for_searching_data').value = '11:00am';
});
_1100am.addEventListener('click', function() {
  document.forms['route_form'].action = '/digital_safari/available_routes/time_1100_am/';
  document.forms['route_form'].submit();
});

_1130am.addEventListener('mouseover', function(){
  document.getElementById('for_searching_data').value = '11:30am';
});
_1130am.addEventListener('click', function() {
  document.forms['route_form'].action = '/digital_safari/available_routes/time_1130_am/';
  document.forms['route_form'].submit();
});

_1200pm.addEventListener('mouseover', function(){
  document.getElementById('for_searching_data').value = '12:00pm';
});
_1200pm.addEventListener('click', function() {
  document.forms['route_form'].action = '/digital_safari/available_routes/time_1200_pm/';
  document.forms['route_form'].submit();
});

_1230pm.addEventListener('mouseover', function(){
  document.getElementById('for_searching_data').value = '12:30pm';
});
_1230pm.addEventListener('click', function() {
  document.forms['route_form'].action = '/digital_safari/available_routes/time_1230_pm/';
  document.forms['route_form'].submit();
});

_1300pm.addEventListener('mouseover', function(){
  document.getElementById('for_searching_data').value = '13:00pm';
});
_1300pm.addEventListener('click', function() {
  document.forms['route_form'].action = '/digital_safari/available_routes/time_1300_pm/';
  document.forms['route_form'].submit();
});

_1330pm.addEventListener('mouseover', function(){
  document.getElementById('for_searching_data').value = '13:30pm';
});
_1330pm.addEventListener('click', function() {
  document.forms['route_form'].action = '/digital_safari/available_routes/time_1330_pm/';
  document.forms['route_form'].submit();
});

_1400pm.addEventListener('mouseover', function(){
  document.getElementById('for_searching_data').value = '14:00pm';
});
_1400pm.addEventListener('click', function() {
  document.forms['route_form'].action = '/digital_safari/available_routes/time_1400_pm/';
  document.forms['route_form'].submit();
});

_1430pm.addEventListener('mouseover', function(){
  document.getElementById('for_searching_data').value = '14:30pm';
});
_1430pm.addEventListener('click', function() {
  document.forms['route_form'].action = '/digital_safari/available_routes/time_1430_pm/';
  document.forms['route_form'].submit();
});

_1500pm.addEventListener('mouseover', function(){
  document.getElementById('for_searching_data').value = '15:00pm';
});
_1500pm.addEventListener('click', function() {
  document.forms['route_form'].action = '/digital_safari/available_routes/time_1500_pm/';
  document.forms['route_form'].submit();
});

_1530pm.addEventListener('mouseover', function(){
  document.getElementById('for_searching_data').value = '15:30pm';
});
_1530pm.addEventListener('click', function() {
  document.forms['route_form'].action = '/digital_safari/available_routes/time_1530_pm/';
  document.forms['route_form'].submit();
});

_1600pm.addEventListener('mouseover', function(){
  document.getElementById('for_searching_data').value = '16:00pm';
});
_1600pm.addEventListener('click', function() {
  document.forms['route_form'].action = '/digital_safari/available_routes/time_1600_pm/';
  document.forms['route_form'].submit();
});

_1630pm.addEventListener('mouseover', function(){
  document.getElementById('for_searching_data').value = '16:30pm';
});
_1630pm.addEventListener('click', function() {
  document.forms['route_form'].action = '/digital_safari/available_routes/time_1630_pm/';
  document.forms['route_form'].submit();
});

_1700pm.addEventListener('mouseover', function(){
  document.getElementById('for_searching_data').value = '17:00pm';
});
_1700pm.addEventListener('click', function() {
  document.forms['route_form'].action = '/digital_safari/available_routes/time_1700_pm/';
  document.forms['route_form'].submit();
});

_1730pm.addEventListener('mouseover', function(){
  document.getElementById('for_searching_data').value = '17:30pm';
});
_1730pm.addEventListener('click', function() {
  document.forms['route_form'].action = '/digital_safari/available_routes/time_1730_pm/';
  document.forms['route_form'].submit();
});

_1800pm.addEventListener('mouseover', function(){
  document.getElementById('for_searching_data').value = '18:00pm';
});
_1800pm.addEventListener('click', function() {
  document.forms['route_form'].action = '/digital_safari/available_routes/time_1800_pm/';
  document.forms['route_form'].submit();
});

_1830pm.addEventListener('mouseover', function(){
  document.getElementById('for_searching_data').value = '18:30pm';
});
_1830pm.addEventListener('click', function() {
  document.forms['route_form'].action = '/digital_safari/available_routes/time_1830_pm/';
  document.forms['route_form'].submit();
});

_1900pm.addEventListener('mouseover', function(){
  document.getElementById('for_searching_data').value = '19:00pm';
});
_1900pm.addEventListener('click', function() {
  document.forms['route_form'].action = '/digital_safari/available_routes/time_1900_pm/';
  document.forms['route_form'].submit();
});

_1930pm.addEventListener('mouseover', function(){
  document.getElementById('for_searching_data').value = '19:30pm';
});
_1930pm.addEventListener('click', function() {
  document.forms['route_form'].action = '/digital_safari/available_routes/time_1930_pm/';
  document.forms['route_form'].submit();
});

_2000pm.addEventListener('mouseover', function(){
  document.getElementById('for_searching_data').value = '20:00pm';
});
_2000pm.addEventListener('click', function() {
  document.forms['route_form'].action = '/digital_safari/available_routes/time_2000_pm/';
  document.forms['route_form'].submit();
});

_2030pm.addEventListener('mouseover', function(){
  document.getElementById('for_searching_data').value = '20:30pm';
});
_2030pm.addEventListener('click', function() {
  document.forms['route_form'].action = '/digital_safari/available_routes/time_2030_pm/';
  document.forms['route_form'].submit();
});


















});
