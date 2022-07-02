$(document).ready(function() {
	var max_fields      = 100; //maximum input boxes allowed
	var wrapper_brd   		= $(".input_fields_wrap_board"); //Fields wrapper
	var wrapper_ins   		= $(".input_fields_wrap_installment"); //Fields wrapper
	var add_button_board      = $(".add_field_button_board"); //Add button ID
	var add_button_installment      = $(".add_field_button_installment"); //Add button ID
	const TargetForm = document.getElementsByClassName('boardul');
	// const EmptyForm = document.getElementById('boardli').cloneNode('True');
	// Counttarget = EmptyForm.querySelector('#btitle');
	// $(Counttarget).append(' ' + x); //add input box
	const TargetFormi = document.getElementsByClassName('insul');
	// const EmptyFormi = document.getElementById('insli').cloneNode('True');
	// Counttargeti = EmptyFormi.querySelector('#ititle');
	// $(Counttargeti).append(' ' + y); //add input box
	var checkboxdata      = $(".checkboxdata"); //Add button ID

	const TotalForms2 = document.getElementById('id_formset2-TOTAL_FORMS')
	TotalForms2.setAttribute('value',0)
	const TotalForms3 = document.getElementById('id_formset3-TOTAL_FORMS')
	TotalForms3.setAttribute('value',0)


	$(add_button_board).click(function(e){ //on add input button click
		e.preventDefault();
			const CountForms= document.getElementsByClassName('boardli').length -1;
			const Titl = document.getElementsByClassName('boardli').length;
			const TotalNewForms = document.getElementById('id_formset2-TOTAL_FORMS')

			const EmptyForm = document.getElementById('boardli').cloneNode('True');
			EmptyForm.setAttribute('class','boardli');
			EmptyForm.setAttribute('id',`formb-${CountForms}`);
			const JDatepicker = EmptyForm.querySelector('.JalaliStart');
			JDatepicker.setAttribute('id','JalaliStart'+ CountForms);
			const JDatepickerSep = EmptyForm.querySelector('.JalaliFinish');
			JDatepickerSep.setAttribute('id','JalaliFinish'+ CountForms);

			$(EmptyForm).append('<button href="#" class="remove_field">حذف</button><script type="text/javascript">kamaDatepicker("JalaliStart'+ CountForms +'" , {buttonsColor: "red",forceFarsiDigits: true}); kamaDatepicker("JalaliFinish'+ CountForms +'", {buttonsColor: "red",forceFarsiDigits: true});</script>'); //add input box
			const regex = new RegExp('__prefix__','g')
			EmptyForm.innerHTML = EmptyForm.innerHTML.replace(regex,CountForms)
			TotalNewForms.setAttribute('value',Titl)
			SeacrhableClass = EmptyForm.querySelector(`#id_formset2-${CountForms}-BoardID`);
			SeacrhableClass.setAttribute('class','searchable');
			$(EmptyForm).append('<script type="text/javascript">$(document).ready(function() {$(".searchable").select2();});</script>');
			$(TargetForm).append(EmptyForm); //add input box
			Counttarget = EmptyForm.querySelector('#btitle');
			$(Counttarget).append(' ' + Titl ); //add input box



		});
	$(add_button_installment).click(function(e){ //on add input button click
		e.preventDefault();


			const CountForms= document.getElementsByClassName('insli').length -1;
			const Titl = document.getElementsByClassName('insli').length;
			const TotalNewForms = document.getElementById('id_formset3-TOTAL_FORMS')
			const EmptyFormi = document.getElementById('insli').cloneNode('True');
			EmptyFormi.setAttribute('class','insli');
			EmptyFormi.setAttribute('id',`form-${CountForms}`);
			const JDatepickerSepi = EmptyFormi.querySelector('.PaymentDateJalali');
			 JDatepickerSepi.setAttribute('id','PaymentDateJalali'+ CountForms);
			$(EmptyFormi).append('<button href="#" class="remove_field">حذف</button><script type="text/javascript">kamaDatepicker("PaymentDateJalali'+ CountForms +'", {buttonsColor: "red",forceFarsiDigits: true});</script>'); //add input box
			const regex = new RegExp('__prefix__','g')
			EmptyFormi.innerHTML = EmptyFormi.innerHTML.replace(regex,CountForms)
			TotalNewForms.setAttribute('value',Titl)
			$(TargetFormi).append(EmptyFormi); //add input box
			Counttargeti = EmptyFormi.querySelector('#ititle');
			$(Counttargeti).append(' ' + Titl ); //add input box

		});
	$(TargetForm).on("click",".remove_field", function(e){ //user click on remove text
		e.preventDefault(); $(this).parent('li').remove();
	})
	$(TargetFormi).on("click",".remove_field", function(e){ //user click on remove text
		e.preventDefault(); $(this).parent('li').remove();
	})



});
