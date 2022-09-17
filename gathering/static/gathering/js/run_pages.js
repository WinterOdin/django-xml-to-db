
function runPackage(url_data) {

	function convertToCSV(arr) {
		const array = [Object.keys(arr[0])].concat(arr);
		return array.map(it => {
			return Object.values(it).toString().replace(/[\r\n]+/g, "");
		}).join('\n')
	}

	$("#clear-form").on("click", function() {
		$('#id_entry').val('');
	});

	$("#input-form").submit(function(e) {
		e.preventDefault();
		var serializedData = $(this).serialize();

		$.ajax({
			type: 'POST',
			url: url_data,
			headers: {
				"X-Requested-With": "XMLHttpRequest",
			},
			data: serializedData,
			success: function(response) {
				var tableData = response['available_data'];

				build(tableData)
				
				$('#download_csv').show();


				$('#download_csv').on("click", function() {
					var data = convertToCSV(response['available_data']);
					var uri = 'Data:text/csv;charset=utf-8,' + escape(data);
					var link = document.createElement("a");
					link.href = uri;
					link.style = "visibility:hidden";
					link.download = 'data.csv';
					document.body.appendChild(link);
					link.click();
					document.body.removeChild(link);
				});

				$('#welcome-note').fadeOut('fast');
				setTimeout(function() {
					$('#content-container').fadeIn('fast');
					$('#pagination-wrapper').fadeIn('fast');
					$('#download_csv').fadeIn('slow');

				}, 200);
			},
			error: function(response) {
				console.log(response)
			}
		})
	})


	$(document).ajaxStart(function() {

		$('#download_csv').fadeOut('slow');
		//not $('#content-container, #pagination-wrapper') because it changing in wrong way
		$('#content-container').fadeOut(100, function() {
			$('#table-body, #pagination-wrapper').empty();
		});

	});
}