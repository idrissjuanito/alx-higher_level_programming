$(function() {
	handleEvent = function (value=null) {
		const val = value ?? $('INPUT#language_code').val()
		$.ajax({
			type: 'GET',
			url: 'http://hellosalut.stefanbohacek.dev/?lang='+val,
			success: function(data) {
				$('DIV#hello').text(data.hello)
			}
		})
	}
	$('INPUT#btn_translate').click(() => handleEvent(null))
	$('INPUT#language_code').focus(function(e) {
		$('INPUT#language_code').keyup(function(e) {
			if (e.which == 13) handleEvent(e.target.value)
		})
	})
	
})
