import React from 'react';
import System from './components/System/System';
import LEDControls from './components/LEDControls/LEDControls';

const App = () => {
  return (
    <div>
      <LEDControls />
      <System />
    </div>
  )
}

export default App