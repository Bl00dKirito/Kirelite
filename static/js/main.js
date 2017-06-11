(function() {

	var bodyEl = document.body,
		content = document.querySelector( '.content-wrap' ),
		openbtn = document.getElementById( 'litebar-button' ),
		isOpen = false;
	openbtn.style.transition = "opacity 1s";


	var SW = new SiriWave({
		width: 800,
		height: 200,
		speed: 0.1,
		amplitude: 1,
		speedInterpolationSpeed: 0,
		container: document.getElementById('siric'),
		autostart: true,
	});

	var ctx = new (window.AudioContext || window.webkitAudioContext)();
	var analyser = ctx.createAnalyser();
	analyser.connect(ctx.destination);
	analyser.fftSize = 2048;

	var bufferLength = analyser.frequencyBinCount;
	function getAverageVolume(data) {
		var values = 0;
		var length = data.length;
		for (var i = 0; i < data.length; i++) {
			values += data[i];
		}
		return values / data.length;
	}

	function init() {
		initEvents();
	}

	function initEvents() {
		openbtn.addEventListener( 'click', toggleMenu );
		content.addEventListener( 'click', function(ev) {
			var target = ev.target;
			if( isOpen && target !== openbtn ) {
				toggleMenu();
			}
		} );
	}

	function toggleMenu() {
		if( isOpen ) {
			classie.remove( bodyEl, 'show-litebar' );
			openbtn.style.opacity=1;
			openbtn.disabled = false;
		}
		else {
			classie.add( bodyEl, 'show-litebar' );
			openbtn.style.opacity=0;
			openbtn.disabled = true;
		}
		isOpen = !isOpen;
	}

	init();

	window.navigator.getUserMedia({ audio: true },
	function(stream) {
		var input = ctx.createMediaStreamSource(stream);
		input.connect(analyser);

		var processor = ctx.createScriptProcessor(2048, 1, 1);
		processor.connect(ctx.destination);

		processor.onaudioprocess = function() {
			var array =  new Uint8Array(analyser.frequencyBinCount);
			analyser.getByteFrequencyData(array);
			var average = getAverageVolume(array);
			SW.setAmplitude(average / 140);
		};
   },
	function(){}
	);

})();
