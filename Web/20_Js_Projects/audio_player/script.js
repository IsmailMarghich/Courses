const image = document.querySelector('img');
const title = document.getElementById('title');
const artist = document.getElementById('artist');
const music = document.querySelector('audio');
const progressContainer = document.getElementById('progress-container');
const progress = document.getElementById('progress');
const currentTimeElement = document.getElementById('current-time');
const durationElement = document.getElementById('duration');
const prevBtn = document.getElementById('prev');
const playBtn = document.getElementById('play');
const nextBtn = document.getElementById('next');

// Array of objects with our music
const songs = [
    {
        name: 'Allahu',
        displayName: 'Allahu',
        artist: 'Ahmadullah Awan'
    },
    {
        name: 'Dream',
        displayName: 'Dream Seduced',
        artist: 'Muhammad Al Muqit'
    },
    {
        name: 'Mawla',
        displayName: 'Maula Ya Salli Wa Sallim',
        artist: 'Mohammed Al Hisayan'
    }
]

//Boolean to check if playing
let isPlaying = false;
// Play
const playSong = () => {
    isPlaying = true;
    playBtn.classList.replace('fa-play', 'fa-pause')
    playBtn.setAttribute('title', 'Pause')
    music.play();
}
// Pause
const pauseSong = () => {
    isPlaying = false;
    playBtn.classList.replace('fa-pause', 'fa-play')
    playBtn.setAttribute('title', 'Play')
    music.pause();
}

//Event listeners
/*Play or pause event listener*/
playBtn.addEventListener('click', () =>{
    (isPlaying ? pauseSong(): playSong()) /*if the song is playing, pause, if its not playing, play*/
    }
)
// Update DOM with songs
const loadSong = (song) =>{
    title.textContent = song.displayName;
    artist.textContent= song.artist;
    music.src = `music/${song.name}.mp3`;
    image.src = `img/${song.name}.png`;
}
//Current song
let songIndex = 0;

// Next song

const nextSong = ()=>{
    if (songIndex === songs.length - 1){ /*if we reach final song, go to first song*/
        songIndex = -1;
    }
    songIndex++;
    loadSong(songs[songIndex]);
    playSong();
}

//Previous song
const prevSong = ()=>{
    if (songIndex === 0){ /*if we try to go back from first song, go to last song*/
        songIndex = songs.length;
    }
    songIndex--;
    loadSong(songs[songIndex]);
    playSong();
}
// On load, select first song
loadSong(songs[songIndex]);

// Update progress bar and time
const updateProgressBar = (e) => {
    if (isPlaying){
        const { duration, currentTime} = e.target; /*grab duration and current time of song from event*/
        //Update progress bar width
        const progressPercent = (currentTime / duration) * 100;
        progress.style.width = `${progressPercent}%`;
        //Calculate display for duration
        const durationMinutes = Math.floor(duration / 60); /*calculate minutes and round down*/
        let durationSeconds = Math.floor(duration % 60);
        if (durationSeconds < 10){ /*if its under 10, and such there is only 1 digit*/
            durationSeconds = `0${durationSeconds}` /*make it into a string with 0 as first digit*/
        }
        //Delay switching duration element to avoid NaN while numbers are still being calculated
        if (durationSeconds){
            durationElement.textContent = `${durationMinutes}:${durationSeconds}`
        }
        const currentMinutes = Math.floor(currentTime / 60); /*calculate minutes and round down*/
        let currentSeconds = Math.floor(currentTime % 60);
        if (currentSeconds < 10){ /*if its under 10, and such there is only 1 digit*/
            currentSeconds = `0${currentSeconds}` /*make it into a string with 0 as first digit*/
        }
        currentTimeElement.textContent = `${currentMinutes}:${currentSeconds}`
    }
}

const setProgressBar = (e)=>{
    const width = e.target.clientWidth;
    const clickX = e.offsetX;
    const {duration} = music;
    music.currentTime = (clickX / width) * duration;
}
// Event Listeners
prevBtn.addEventListener('click', prevSong);
nextBtn.addEventListener('click', nextSong)
music.addEventListener('ended', nextSong) /*if we reach end of song, go to next song*/
music.addEventListener('timeupdate', updateProgressBar);
progressContainer.addEventListener("click", setProgressBar);