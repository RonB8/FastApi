<audio id="myAudio" controls>
  <source src="C:/Users/user/Downloads/Between 1984 1988 Ne.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

<script>
  // יצירת עצםם של AudioContext
  const audioContext = new (window.AudioContext || window.webkitAudioContext)();

  // משתנה המקיים את האובייקט הקשור לנגן
  const audioElement = document.getElementById('myAudio');

  // קביעת ה-HTMLAudioElement כמקור של הנתונים הקוליים
  const audioSource = audioContext.createMediaElementSource(audioElement);

  // יצירת AnalyzerNode שמאפשר לנו לבצע אנליזה על הצליל
  const analyzer = audioContext.createAnalyser();
  audioSource.connect(analyzer);
  analyzer.connect(audioContext.destination);

  // קביעת מספר הדגימות שייאסף על ידי הAnalyzerNode
  analyzer.fftSize = 256;
  const bufferLength = analyzer.frequencyBinCount;
  const dataArray = new Uint8Array(bufferLength);

  // פונקציה המזהה רגעים של שקט
  function detectSilence() {
    analyzer.getByteFrequencyData(dataArray);
    let sum = dataArray.reduce((acc, val) => acc + val, 0);
    let average = sum / bufferLength;
    if (average < 10) {
      console.log("Silence detected");
    } else {
      console.log("Sound detected");
    }
    requestAnimationFrame(detectSilence);
  }

  // פתיחת נגן הקובץ האודיו
  audioElement.play();
  // קריאה לפונקציה לזיהוי השקט
  detectSilence();
</script>
