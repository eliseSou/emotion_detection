import './index.css';
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

import "./i18n";
import { ChakraProvider } from '@chakra-ui/react';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);

root.render(
  <ChakraProvider>
    <App />
  </ChakraProvider>
);
