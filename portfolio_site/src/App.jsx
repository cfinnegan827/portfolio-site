import './App.scss';
import acadiaImg1 from './assets/acadia/acadia1.JPG';
import arubaImg1 from './assets/aruba/aruba1.JPG';
import maineImg1 from './assets/maine/maine1.JPG';

function App() {
  return (
    <div className='container'>
      <div className='home_container'>
        <div className='home'>
          <div className='title'>
            <div className='name'><h1>Connor Finnegan</h1></div>
          </div>
          <div className="context">
            <div className='quick_links'>
              <h2> Quick Links</h2>
              <ul>
                <p>Socials</p>
                <li>Github</li>
                <li>LinkedIn</li>
                <p>Pages</p>
                <li>Projects</li>
                <a href='#work'><li>Work Experience</li></a>
                <a href='#travel'><li>Travel</li></a>
                <li>Contact Info</li>
              </ul>
            </div>
            <div className='description'>
            <p>Hi! My name is Connor, I am a computer science alumni from Umass Boston. I
              am currently working as an IT Coordinator at East Cambridge Savings Bank. Where
              I work hands on resolving user issues ranging from password resets and account lockouts to more severe problems
              like permission and network access issues, hardware and software support, as well as general technical questions users
              may have. In this role I also work on projects, with the main ones right now being a company wide computer conversion, where 
              I work on creating and deploying images onto computers, download department specific software, and then swap out users computer.
              As well as banking software permission project, where I am working on documenting permissions created by a third party banking
              software used by a majority of users so I can consolidate them into department specific permissions which helps streamline the
              onboarding process for new users. Using my programming knowledge to create a data pipeline to extract permission data and clean
              it using the python pandas library to use in the permission editing and reporting for audit purposes.
            </p>
            </div>
          </div>
        </div>
      </div>

    <div className='work' id='work'>
      <h1>This is some test text</h1>
      <div className="experience">
        <h1>Title</h1>
      </div>
    </div>
      <div className='travel' id='travel'>
        <div className='travel_card_container'>
        <div className='travel_card'><img src={acadiaImg1} alt='acadia'/><h2>Acadia</h2></div>
        <div className='travel_card'><img src={arubaImg1} alt='acadia'/><h2>Aruba</h2></div>
        <div className='travel_card'><img src={maineImg1} alt='acadia'/><h2>York</h2></div>
        </div>
        <div className='travel_more'></div>
      </div>
    </div>
  );
}

export default App;
