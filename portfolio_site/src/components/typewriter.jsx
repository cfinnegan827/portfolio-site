import React, { useState, useEffect } from 'react';

// code used from the geeksforgeeks website
// https://www.geeksforgeeks.org/reactjs/how-to-create-typewriter-effect-in-reactjs/
const TypewriterEffect = ({ text, speed }) => {
    const [displayedText, setDisplayedText] = useState('');
    const [index, setIndex] = useState(0);

    useEffect(() => {
        const interval = setInterval(() => {

            if (index < text.length) {
                setDisplayedText((prev) => prev + text[index]);
                setIndex(index + 1);
            } else {
                clearInterval(interval);
            }
        }, speed);

        return () => clearInterval(interval);
    }, [index, text, speed]);

    return <span className="typewriter-text">{displayedText}</span>;
};

export default TypewriterEffect;