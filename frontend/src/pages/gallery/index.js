import React from 'react';
import Card from './card';
import Jumbutron from '../../components/Jumbutron'; 
import SearchField from "../../components/SearchField";

const ImagePage = () => {
  return (
    <div>
      <Jumbutron>
        <SearchField />
      </Jumbutron>

      <div className="card-container">
      <Card
          imageUrl="https://picsum.photos/200"
          title="Sample Image 1"
        />
      </div>

      

      


    </div>
  );
};

export default ImagePage;
