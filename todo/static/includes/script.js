function calcDS() {
  var imageNum = document.getElementsByClassName("allItems").length;
  console.log(imageNum);
  var ds = imageNum * 0.5;
  localStorage.setItem("ds",ds);
}

function updateKG()
{
  var dark = "0 Kg";
  var litghtSoft = "0 Kg";
  var darkSoft = localStorage.getItem("ds") + " kg";

  var pD = document.createElement("p");
  pD.append(dark);
  document.getElementsByClassName("baskets")[0].appendChild(pD);

  var pLs = document.createElement("p");
  pLs.append(litghtSoft);
  document.getElementsByClassName("baskets")[1].appendChild(pLs);

  var pDs = document.createElement("p");
  if (localStorage.getItem("ds") != null)
    pDs.append(darkSoft);
  else
    pDs.append(dark);
  document.getElementsByClassName("baskets")[2].appendChild(pDs);
}

/*---------- form---------*/ 
$(document).ready(function(){
    $("#myForm").multiStepForm(
    {
      // defaultStep:0,
      callback : function(){
      }
    }
    ).navigateTo(0);
  });
  
  
  
  (function ( $ ) {
    $.fn.multiStepForm = function(args) {
        if(args === null || typeof args !== 'object' || $.isArray(args))
          throw  " : Called with Invalid argument";
        var form = this;
        var tabs = form.find('.tab');
        var steps = form.find('.step');
        steps.each(function(i, e){
          $(e).on('click', function(ev){
            form.navigateTo(i);
          });
        });
        form.navigateTo = function (i) {/*index*/
          /*Mark the current section with the class 'current'*/
          tabs.removeClass('current').eq(i).addClass('current');
          // Show only the navigation buttons that make sense for the current section:
          form.find('.previous').toggle(i > 0);
          atTheEnd = i >= tabs.length - 1;
          form.find('.next').toggle(!atTheEnd);
          // console.log('atTheEnd='+atTheEnd);
          form.find('.submit').toggle(atTheEnd);
          fixStepIndicator(curIndex());
          return form;
        }
        function curIndex() {
          /*Return the current index by looking at which section has the class 'current'*/
          return tabs.index(tabs.filter('.current'));
        }
        function fixStepIndicator(n) {
          steps.each(function(i, e){
            i == n ? $(e).addClass('active') : $(e).removeClass('active');
          });
        }
        /* Previous button is easy, just go back */
        form.find('.previous').click(function() {
          form.navigateTo(curIndex() - 1);
        });
  
        /* Next button goes forward iff current block validates */
        form.find('.next').click(function() {
          if('validations' in args && typeof args.validations === 'object' && !$.isArray(args.validations)){
            if(!('noValidate' in args) || (typeof args.noValidate === 'boolean' && !args.noValidate)){
              form.validate(args.validations);
              if(form.valid() == true){
                form.navigateTo(curIndex() + 1);
                return true;
              }
              return false;
            }
          }
          form.navigateTo(curIndex() + 1);
        });
        form.find('.submit').on('click', function(e){
          if(typeof args.beforeSubmit !== 'undefined' && typeof args.beforeSubmit !== 'function')
            args.beforeSubmit(form, this);
          /*check if args.submit is set false if not then form.submit is not gonna run, if not set then will run by default*/        
          if(typeof args.submit === 'undefined' || (typeof args.submit === 'boolean' && args.submit)){
            form.submit();
          }
          return form;
        });
        /*By default navigate to the tab 0, if it is being set using defaultStep property*/
        typeof args.defaultStep === 'number' ? form.navigateTo(args.defaultStep) : null;
  
        form.noValidate = function() {
          
        }
        return form;
    };
}( jQuery ));

$(document).ready(function () {
  $(".items").hide();
  $("#Arrow").click(function () {
      $(".items").toggle();
  });
})

$('#id_basket').click(function () {
  $.ajax({
      'async': false,
      'global': false,
      'url': "/static/json/data.json",
      'dataType': "json",
      'success': function (data) {

          for (var x = 0; x < data.length; x++) {
              var el = document.createElement('option');
              console.log(data[x]['BASKET']);
              el.setAttribute('value', data[x]['BASKET']);
              console.log(el);
              el.innerHTML = data[x]['BASKET'];
              $("#id_basket").append(el);
          }
      },
      'error': function (data) { alert(data) }
  });
});