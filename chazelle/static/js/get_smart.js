/* Keeps contents of "container" from sliding off to the right when the window size
	is less than container's width.
*/
function centerContainer() {
	var width = window.innerWidth;
	if (typeof(document.body.clientWidth) == 'number') {
    	// newest gen browsers
    	width = document.body.clientWidth;
	}

	var container = document.getElementById('maincontainer');
	if(container == null) {
		container = document.getElementById('puzzcontainer');
	}

	if(width < 1000) {
		var offset = (width-1000)/2;
		container.setAttribute("style", "margin-left:" + offset.toString() + "px");
	} else {
		container.setAttribute("style", "margin-left:auto");
	}
}

function callin() {
	console.log("callin");
}