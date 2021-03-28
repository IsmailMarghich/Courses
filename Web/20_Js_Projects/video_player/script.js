const player = document.querySelector(".player");
const video = document.querySelector("video");
const progressRange = document.querySelector(".progress-range");
const progressBar = document.querySelector(".progress-bar");
const playButton = document.getElementById("play-btn");
const volumeIcon = document.getElementById("volume-icon");
const volumeRange = document.querySelector(".volume-range");
const volumeBar = document.querySelector(".volume-bar");
const currentTime = document.querySelector(".time-elapsed");
const duration = document.querySelector(".time-duration");
const speed = document.querySelector(".player-speed");
const fullscreenBtn = document.querySelector(".fullscreen");
// Play & Pause ----------------------------------- //

/*change up play and pause button based on video playing*/
const showPlayButton = () => {
    playButton.classList.replace('fa-pause', 'fa-play')
    playButton.setAttribute('title', 'Play')
}

const togglePlay = () => {
    if (video.paused){
        video.play();
        playButton.classList.replace('fa-play', 'fa-pause')
        playButton.setAttribute('title', 'Pause')
    }
    else {
        video.pause();
        showPlayButton();
    }
}
/*On video end, show playButton icon*/
video.addEventListener('ended', showPlayButton);

/*Calculate display time format*/
const displayTime = (time) =>{
    const minutes = Math.floor(time / 60);
    let seconds = Math.floor(time % 60);
    seconds = seconds > 9 ? seconds : `0${seconds}`; /*add a zero if seconds is under 10*/
    return `${minutes}:${seconds}`; /*template string to display*/
}
// Progress Bar ---------------------------------- //
const updateProgress = () => { /*update progress bar as video plays*/
    progressBar.style.width = `${video.currentTime / video.duration * 100}%` /*use a string and % to change progress bar based on time in video*/
    /*pass current and full time of video to display function, and then update DOM*/
    currentTime.textContent = `${displayTime(video.currentTime)} /`;
    duration.textContent= `${displayTime(video.duration)}`;
}

const setProgress = (e) => {
    const newTime = e.offsetX / progressRange.offsetWidth; /*this returns a ratio which we can use to change progress*/
    progressBar.style.width = `${newTime * 100}%`; /*change progressbar visually*/
    video.currentTime = newTime * video.duration /*change progress of video by calculating time*/
}
// Volume Controls --------------------------- //

/*Volume bar*/
let lastVolume = 1 /*var for whether sound on/off*/

const changeVolume = (e) => {
    let volume = e.offsetX / volumeRange.offsetWidth /*volume is ratio of the bar u press on*/
    /*Rounding volume up or down*/
    if (volume < 0.1){
        volume = 0;
    }
    if (volume > 0.9){
        volume = 1;
    }
    volumeBar.style.width = `${volume * 100}%` /*change width based on volume %*/
    video.volume = volume; /*set volume of video*/
    lastVolume = volume;
    /*change volume icon depending on volume*/
    volumeIcon.className = '';
    if(volume > 0.7){
        volumeIcon.classList.add('fas','fa-volume-up')
    }
    if(volume < 0.7 && volume >  0){
        volumeIcon.classList.add('fas','fa-volume-down')

    }else if(volume === 0){
        volumeIcon.classList.add('fas','fa-volume-off')
    }
    lastVolume = volume; /*make sure to update volume boolean after changing volume*/
}
/*Mute/unmute*/

const toggleMute = () => {
    volumeIcon.className = ''; /*reset classes*/
    if (video.volume) { /*trigger if volume is anything but zero*/
        lastVolume = video.volume
        video.volume = 0; /*mute*/
        volumeBar.style.width = 0;
        volumeIcon.classList.add('fas','fa-volume-mute')
        volumeIcon.setAttribute('title', 'Unmute')
    } else {
        video.volume = lastVolume; /*unmute*/
        volumeBar.style.width = `${lastVolume * 100}%` /*get % of volumebar*/
        volumeIcon.classList.add('fas','fa-volume-up')
        volumeIcon.setAttribute('title', 'Mute')

    }
}

// Fullscreen ------------------------------- //
function openFullscreen(elem) {
    if (elem.requestFullscreen) {
        elem.requestFullscreen();
    } else if (elem.webkitRequestFullscreen) { /* Safari */
        elem.webkitRequestFullscreen();
    } else if (elem.msRequestFullscreen) { /* IE11 */
        elem.msRequestFullscreen();
    }
    video.classList.add('video-fullscreen') /*make video fill up the whole screen*/
}

/* Close fullscreen */
function closeFullscreen() {
    if (document.exitFullscreen) {
        document.exitFullscreen();
    } else if (document.webkitExitFullscreen) { /* Safari */
        document.webkitExitFullscreen();
    } else if (document.msExitFullscreen) { /* IE11 */
        document.msExitFullscreen();
    }
    video.classList.remove('video-fullscreen') /*make video small again*/
}
let fullscreen = false; /*boolean for fullscreen or not*/
/*Toggle fullscreen*/
const toggleFullscreen = () => {
    if (!fullscreen){
        openFullscreen(player)
    }else {
        closeFullscreen();
    }
    fullscreen = !fullscreen /*reverse value of fullscreen boolean*/
}
/*Event listeners*/
playButton.addEventListener('click', togglePlay);
video.addEventListener('click', togglePlay); /*make it so we can pause and play whenever we click on the video*/
video.addEventListener('timeupdate', updateProgress); /*everytime time updates, we update progress bar*/
video.addEventListener('canplay', updateProgress);
progressRange.addEventListener('click', setProgress)
volumeRange.addEventListener('click', changeVolume);
volumeIcon.addEventListener('click', toggleMute);
speed.addEventListener('change', () => {
    video.playbackRate = speed.value; /*set video playback rate to value of select*/
});
fullscreenBtn.addEventListener('click', toggleFullscreen);