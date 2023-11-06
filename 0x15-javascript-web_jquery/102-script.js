$(function() {
	$('INPUT#btn_translate').click(function() {
		const val = $('INPUT#language_code').val()
		$.ajax({
			type: 'GET',
			url: 'http://hellosalut.stefanbohacek.dev/?lang='+val,
			success: function(data) {
				$('DIV#hello').text(data.hello)
			}
		})
	})
})
