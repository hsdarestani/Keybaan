$(document).ready(function() {
	var max_fields      = 100; //maximum input boxes allowed
	var wrapper_brd   		= $(".input_fields_wrap_board"); //Fields wrapper
	var wrapper_ins   		= $(".input_fields_wrap_installment"); //Fields wrapper
	var add_button_board      = $(".add_field_button_board"); //Add button ID
	var add_button_installment      = $(".add_field_button_installment"); //Add button ID

	var x = 1; //initlal text box count
	$(add_button_board).click(function(e){ //on add input button click
		e.preventDefault();
		if(x < max_fields){ //max input box allowed
			x++; //text box increment
			$(wrapper_brd).append('<li class="boardli"><a href="#" class="remove_field">حذف</a></span><input type="checkbox"><i></i><h4>تابلوی '+ (x) +'</h4><p><span class="row"><input class="col-md-6 col-sm-6 col-xs-6 w55" list="LocationID" name="LocationID" placeholder="نام جایگاه"><datalist id="LocationID"><option value="جایگاه 1"><option value="جایگاه 2"><option value="جایگاه 3"><option value="جایگاه 4"><option value="جایگاه 5"></datalist><input class="col-md-6 col-sm-6 col-xs-6 w40" list="BoardID" name="BoardID" placeholder="کد تابلو"><datalist id="BoardID"><option value="تابلوی 1"><option value="تابلوی 2"><option value="تابلوی 3"><option value="تابلوی 4"><option value="تابلوی 5"></datalist></span><br><br><span class="row"><input class="col-md-4 col-sm-4 col-xs-6 kbforms" type="text" readonly="readonly" placeholder="تاریخ شروع اکران" id="ContractStartJalali'+ (x) +'"><script type="text/javascript">kamaDatepicker("ContractStartJalali'+ (x) +'", {buttonsColor: "red",forceFarsiDigits: true});</script></span><br><br><span class="row"><input class="col-md-4 col-sm-4 col-xs-6 kbforms" type="text" readonly="readonly" placeholder="تاریخ پایان اکران" id="ContractFinishJalali'+ (x) +'"><script type="text/javascript">kamaDatepicker("ContractFinishJalali'+ (x) +'", {buttonsColor: "red",forceFarsiDigits: true});</script></span><br><br><span class="row"><input class=" col-md-8 col-sm-8 col-xs-12 kbforms" type="text" id="value" name="value" placeholder="مبلغ قرارداد تابلو"></span><br><br></p></li>'); //add input box
		}
		});
	var y = 1; //initlal text box count
	$(add_button_installment).click(function(e){ //on add input button click
		e.preventDefault();
		if(y < max_fields){ //max input box allowed
			y++; //text box increment
			$(wrapper_ins).append('<li class="boardli"><a href="#" class="remove_field">حذف</a><input type="checkbox" ><i></i><h4>قسط '+ (y) +'</h4><p><span class="row"><input class=" col-md-4 col-sm-4 col-xs-6 w15" type="text" id="value" name="value" placeholder="نوبت قسط"><input class=" col-md-4 col-sm-4 col-xs-6 w40" type="text" id="value" name="value" placeholder="مبلغ قسط"><input class="col-md-4 col-sm-4 col-xs-6 w40" type="text" readonly="readonly" placeholder="تاریخ پرداخت" id="PaymentDateJalali'+ (y) +'"><script type="text/javascript">kamaDatepicker("PaymentDateJalali'+ (y) +'", {buttonsColor: "red",forceFarsiDigits: true});</script></span><br><br></p></span></li>'); //add input box
		}});
	$(wrapper_brd).on("click",".remove_field", function(e){ //user click on remove text
		e.preventDefault(); $(this).parent('li').remove(); x--;
	})
	$(wrapper_ins).on("click",".remove_field", function(e){ //user click on remove text
		e.preventDefault(); $(this).parent('li').remove(); y--;
	})
});
