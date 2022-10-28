
function toggle_view(name) {
	var x = document.getElementsByName(name)
	for (var I=0; I<x.length; I++) {
		if (x[I].style.display == "none")
			x[I].style.display = "block"
		else x[I].style.display = "none"
	}
}
