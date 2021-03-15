const videoElement = document.getElementById('video')
const button = document.getElementById('button')

/*async function to prompt user to select media stream, pass that video element, then play*/
async function selectMediaStream() {
    try {
        const mediaStream = await navigator.mediaDevices.getDisplayMedia(); /*use chooses media*/
        videoElement.srcObject = mediaStream; /*set the video's src to media*/
        videoElement.onloadedmetadata = () => { /*when video is loaded*/
            videoElement.play();
        }
    }catch (e) {
        console.log(e)
    }
}
button.addEventListener('click', async () =>{
    /*disable button*/
    button.disabled = true;
    /*start picture in picture*/
    await videoElement.requestPictureInPicture();
    /*reset button*/
    button.disabled = false;
});
selectMediaStream();