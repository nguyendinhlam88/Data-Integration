var Render = new (function __Render() {
	this.cards = function (items) {
		var html = ``;
		items.forEach(function (item) {
			html += getHTML(item);
		});
		$('#js-list-cards').html(html);
	};
})();

function getHTML(item) {
	return `
		<div class = "col-12 col-sm-6 col-md-4 margin item ">
			<div class = "card shadow-sm p-3 mb-5 bg-white rounded" style = "width: 18rem;">
				<img src = ${item.image} class = "card-img-top img-thumbnail" alt = "..." >
				<div class = "card-body">
					<h5 class = "card-title">${item.title} </h5>
					<p class = "card-text">${item.price} </p>
					<a href = ${item.link} class = "btn btn-primary"> Go to page </a>
				</div>
			</div>
		</div>
	`;
}

var items = [
	{
		title: 'huyndai a200',
		price: '220',
		image:
			'https://img1.oto.com.vn/crop/575x430/2022/06/16/20220616213940-0d0f_wm.jpg',
		link: 'https://www.facebook.com/dlk1705'
	},
	{
		title: 'merc c200',
		price: '120',
		image:
			'https://img1.oto.com.vn/crop/575x430/2022/06/16/20220616213940-0d0f_wm.jpg',
		link: 'https://www.facebook.com/dlk1705'
	},
	{
		title: 'huyndai',
		price: '20',
		image:
			'https://img1.oto.com.vn/crop/575x430/2022/06/16/20220616213940-0d0f_wm.jpg',
		link: 'https://www.facebook.com/dlk1705'
	},

	{
		title: 'test test',
		price: '2220',
		image:
			'https://img1.oto.com.vn/crop/575x430/2022/06/16/20220616213940-0d0f_wm.jpg',
		link: 'https://www.facebook.com/dlk1705'
	}
];

$('#search').on('keyup', function () {
	var value = $(this).val().toLowerCase();
	var rs = items.filter((item) => item.title.toLowerCase().includes(value));
	Render.cards(rs);
});

$('#min-price').on('keyup', function () {
	var min_price = parseInt($(this).val());
	if (isNaN(min_price)) {
		Render.cards(items);
		return;
	}
	var max_price = parseInt($('#max-price').val());
	if (isNaN(max_price)) {
		var rs = items.filter((item) => item.price >= min_price);
		Render.cards(rs);
	} else {
		var rs = items.filter(
			(item) => item.price >= min_price && item.price <= max_price
		);
		Render.cards(rs);
	}
});

$('#max-price').on('keyup', function () {
	var max_price = parseInt($(this).val());
	if (isNaN(max_price)) {
		Render.cards(items);
		return;
	}
	var min_price = parseInt($('#min-price').val());
	if (isNaN(min_price)) {
		var rs = items.filter((item) => item.price <= max_price);
		Render.cards(rs);
	} else {
		var rs = items.filter(
			(item) => item.price >= min_price && item.price <= max_price
		);
		Render.cards(rs);
	}
});

Render.cards(items);
