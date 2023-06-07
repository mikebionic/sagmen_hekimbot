var myAudio = document.getElementById("myAudio");
var blink = document.getElementById("blink");
let sound_queue = [];
let audio_on = false;

$("body").mousemove(function (e) {
    if (!audio_on){
        console.log("audio is on!");
        blink.play();
        audio_on = true;
    }
});

const run_sound_2 = (sound_queue) => {
	myAudio.src = sound_queue[0];
	myAudio.play();
	let soundArrayPos = 0;
	startSoundTimer_2(sound_queue, soundArrayPos);
};

const startSoundTimer_2 = (sound_queue, soundArrayPos) => {
	var mySoundTimer = setInterval(() => {
		if (myAudio.currentTime >= myAudio.duration) {
			if (soundArrayPos < sound_queue.length - 1) {
				soundArrayPos += 1;
				myAudio.src = sound_queue[soundArrayPos];
				myAudio.play();
			} else {
				clearInterval(mySoundTimer);
			}
		}
	}, 10);
};

// run_sound_2(sound_queue);

// if (hasUpdates) {
//     update_html_ui(new_arr);
// }