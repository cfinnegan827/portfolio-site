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
            <div className='nav'>
            </div>
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
                <li>Work Experience</li>
                <li>Contact Info</li>
              </ul>
            </div>
            <div className='description'>
            <p>Hi! My name is Connor I am a senior computer science student at Umass Boston.
              I have a strong interest in backend coding and embedded systems, making small 
              projects with raspberry pi and making a plant monitoring system using a esp32.
              I have experience in a wide range of languages with high proficiency in C, 
              Python, Java. With understanding of C++, Racket, and Javascript and small
              experience with assembly as well as pcb design and pcb assembly. I am currently working
              as an IT clerk at East Cambridge Savings Bank. Working on creating and 
              deploying images onto computers, using Ivanti, that are distributed to branches as part 
              of a larger branch conversion project. Being onsite swapping out the computers. 
              As well as modifying users account in Microsoft Office 365 and Microsoft 
              Active Directory Users and Computers(ADUC), and facilitated vendor calls 
              regarding teller software support and general hardware support.
            </p>
            </div>
            <div className='context_filler'></div>
          </div>
        </div>
      </div>

      <div className='travel' id='travel'>
        <div className='travel_card'><img src={acadiaImg1} alt='acadia'/><h2>Acadia</h2></div>
        <div className='travel_card'><img src={arubaImg1} alt='acadia'/><h2>Aruba</h2></div>
        <div className='travel_card'><img src={maineImg1} alt='acadia'/><h2>York</h2></div>
      </div>
    </div>
  );
}

export default App;
