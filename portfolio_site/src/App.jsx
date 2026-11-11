import './App.scss';
import TypewriterEffect from './components/typewriter';

function App() {
  return (
    <div className='container'>
      <div className='nav'>
        <p><a href='#projects'>Projects</a></p>
        <a href='#work'><p>Work</p></a>
        <a href='#contact'><p>Contact</p></a>
      </div>

      <div className='intro'>
        <h1><TypewriterEffect text={"Connor Finnegan \n\n Under Construction"} speed={100} /></h1>
      </div>

    </div>
  );
}

export default App;
