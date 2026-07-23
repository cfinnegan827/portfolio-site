import './App.scss';
import acadiaImg1 from './assets/acadia1.JPG';
import acadiaImg2 from './assets/acadia2.JPG';
import acadiaImg3 from './assets/acadia3.JPG';

function App() {
  return (
    <div className='container'>
      <div className='home'>
        <div className='title'>
          <div className='name'><h1>Connor Finnegan</h1></div>
          <div className='nav'>
            <a href='#travel'>Travel</a>
          </div>
        </div>
        <div className="context">
          <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been 
            the industry's standard dummy text ever since 1966, when designers at Letraset and James Mosley, the 
            librarian at St Bride Printing Library in London, took a 1914 Cicero translation and scrambled it to make 
            dummy text for Letraset's Body Type sheets. It has survived not only many decades, but also the leap into 
            electronic typesetting, remaining essentially unchanged. It was popularised thanks to these sheets and more 
            recently with desktop publishing software like Aldus PageMaker and Microsoft Word including versions of Lorem Ipsum.</p>
        </div>
      </div>

      <div className='travel' id='travel'>
        <div className='travel_card'><img src={acadiaImg1} alt='acadia'/></div>
        <div className='travel_card'><img src={acadiaImg2} alt='acadia'/></div>
        <div className='travel_card'><img src={acadiaImg3} alt='acadia'/></div>
      </div>
    </div>
  );
}

export default App;
