var Render = new (function __Render() {
	this.init = function () {
		var cars = [];
		var categories = [];
		$.ajax({
			url: 'http://127.0.0.1:5000/api/list',
			success: function (data) {
				data.forEach(function (category) {
					categories.push(category.brand);
					category.samples.forEach(function (car) {
						cars.push(car);
					});
				});
			},
			async: false
		});

		return [categories, cars];
	};

	this.cards = function (cars) {
		var html = ``;

		cars.forEach(function (car) {
			html += getHTML(car);
		});
		$('#js-list-cards').html(html);
	};
})();

function getHTML(car) {
	var img =
		'https://img1.oto.com.vn/crop/575x430/2022/06/16/20220616213940-0d0f_wm.jpg';
	var price = formatCash(String(car.gia_ban));
	var tinh_trang = car.tinh_trang == 'NaN' ? 'Chưa rõ' : car.tinh_trang;
	tinh_trang = tinh_trang ? tinh_trang : car.tinh_trang_xe;
	var so_km_da_di =
		!car.so_km_da_di || car.so_km_da_di == 'NaN' ? 'Chưa rõ' : car.so_km_da_di;
	return `
		<div class = "col-12 col-sm-6 col-md-4 margin car ">
			<div class = "card shadow-sm p-3 mb-5 bg-white rounded" style = "width: 18rem;">
				<img src = ${img} class = "card-img-top img-thumbnail" alt = "..." >
				<div class = "card-body">
					<h5 class = "card-title" title='${car.ten}'>${car.ten}</h5>
					<p class = "card-text"> ${price} </p>

					<a href = ${car.url} class = "btn btn-primary"> Go to page </a>
				</div>
			</div>
		</div>
	`;
}

function formatCash(str) {
	return (
		str
			.split('')
			.reverse()
			.reduce((prev, next, index) => {
				return (index % 3 ? next : next + ',') + prev;
			}) + ' VND'
	);
}

$('#search').on('keyup', function () {
	var value = $(this).val().toLowerCase();
	var rs = cars.filter((car) => car.ten.toLowerCase().includes(value));
	Render.cards(rs);
});

$('#min-price').on('keyup', function () {
	var name = $('#search').val().toLowerCase();
	var rs = cars;
	if (name) {
		rs = cars.filter((car) => car.ten.toLowerCase().includes(name));
	}

	var min_price = parseInt($(this).val() + '000000');
	if (isNaN(min_price) || min_price == 0) {
		Render.cards(rs);
		return;
	}
	var max_price = parseInt($('#max-price').val() + '000000');
	if (isNaN(max_price) || max_price == 0) {
		rs = rs.filter((car) => car.gia_ban >= min_price);
		Render.cards(rs);
	} else {
		var rs = rs.filter(
			(car) => car.gia_ban >= min_price && car.gia_ban <= max_price
		);
		Render.cards(rs);
	}
});

$('#max-price').on('keyup', function () {
	var name = $('#search').val().toLowerCase();
	var rs = cars;
	if (name) {
		rs = cars.filter((car) => car.ten.toLowerCase().includes(name));
	}

	var max_price = parseInt($(this).val() + '000000');
	if (isNaN(max_price) || max_price == 0) {
		Render.cards(rs);
		return;
	}
	var min_price = parseInt($('#min-price').val() + '000000');
	if (isNaN(min_price) || min_price == 0) {
		var rs = rs.filter((car) => car.gia_ban <= max_price);
		Render.cards(rs);
	} else {
		var rs = rs.filter(
			(car) => car.gia_ban >= min_price && car.gia_ban <= max_price
		);
		Render.cards(rs);
	}
});

var [categories, cars] = Render.init();
Render.cards(cars);
console.log('sau', cars);
