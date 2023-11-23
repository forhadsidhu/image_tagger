import React from 'react';
import {JumbotronContent,JumbotronWrapper} from './JumbutronElements';
const Jumbutron = ({ children }) => {
  return (
    <JumbotronWrapper>
      <JumbotronContent>
        {children}
      </JumbotronContent>
    </JumbotronWrapper>
  );
};

export default Jumbutron;
