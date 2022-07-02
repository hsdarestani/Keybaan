$(document).ready(function() {
	var max_fields      = 100; //maximum input boxes allowed
	var wrapper_brd   		= $(".input_fields_wrap_board"); //Fields wrapper
	var wrapper_ins   		= $(".input_fields_wrap_installment"); //Fields wrapper
	var add_button_board      = $(".add_field_button_board"); //Add button ID
	var add_button_installment      = $(".add_field_button_installment"); //Add button ID
	const TargetForm = document.getElementsByClassName('boardul');
	const EmptyForm = document.getElementById('boardli').cloneNode('True');
	Counttarget = EmptyForm.querySelector('#btitle');
	$(Counttarget).append(' ' + x); //add input box
	const TargetFormi = document.getElementsByClassName('insul');
	const EmptyFormi = document.getElementById('insli').cloneNode('True');
	Counttargeti = EmptyFormi.querySelector('#ititle');
	$(Counttargeti).append(' ' + y); //add input box
	var checkboxdata      = $(".checkboxdata"); //Add button ID


	var x = 1; //initlal text box count
	$(add_button_board).click(function(e){ //on add input button click
		e.preventDefault();
		if(x < max_fields){ //max input box allowed
			x++; //text box increment
			const EmptyForm = document.getElementById('boardli').cloneNode('True');
			EmptyForm.setAttribute('class','boardli');
			EmptyForm.setAttribute('id','boardli'+ x);
			$(TargetForm).append(EmptyForm); //add input box
			const JDatepicker = EmptyForm.querySelector('.JalaliStart');
			JDatepicker.setAttribute('id','JalaliStart'+ x);
			JDatepicker.setAttribute('name','JalaliStart'+ x);
			const JDatepickerSep = EmptyForm.querySelector('.JalaliFinish');
			JDatepickerSep.setAttribute('id','JalaliFinish'+ x);
			JDatepickerSep.setAttribute('name','JalaliFinish'+ x);
			const Pricelid = EmptyForm.querySelector('#id_BoardContractPrice');
			Pricelid.setAttribute('name','BoardContractPrice'+ x);
			$(EmptyForm).append('<button href="#" class="remove_field">حذف</button><script type="text/javascript">kamaDatepicker("JalaliStart'+ x +'" , {buttonsColor: "red",forceFarsiDigits: true}); kamaDatepicker("JalaliFinish'+ x +'", {buttonsColor: "red",forceFarsiDigits: true});</script>'); //add input box
			Counttarget = EmptyForm.querySelector('#btitle');
			$(Counttarget).append(' ' + x ); //add input box

		}
		});
	var y = 1; //initlal text box count
	$(add_button_installment).click(function(e){ //on add input button click
		e.preventDefault();
		if(y < max_fields){ //max input box allowed
			y++; //text box increment

			const EmptyFormi = document.getElementById('insli').cloneNode('True');
			EmptyFormi.setAttribute('class','insli');
			EmptyFormi.setAttribute('id','insli'+ y);
			$(TargetFormi).append(EmptyFormi); //add input box
			const JDatepickerSepi = EmptyFormi.querySelector('.PaymentDateJalali');
			JDatepickerSepi.setAttribute('id','PaymentDateJalali'+ y);
			$(EmptyFormi).append('<button href="#" class="remove_field">حذف</button><script type="text/javascript">kamaDatepicker("PaymentDateJalali'+ y +'", {buttonsColor: "red",forceFarsiDigits: true});</script>'); //add input box
			Counttargeti = EmptyFormi.querySelector('#ititle');
			$(Counttargeti).append(' ' + y ); //add input box


		}});
	$(TargetForm).on("click",".remove_field", function(e){ //user click on remove text
		e.preventDefault(); $(this).parent('li').remove(); x--;
	})
	$(TargetFormi).on("click",".remove_field", function(e){ //user click on remove text
		e.preventDefault(); $(this).parent('li').remove(); y--;
	})



});
