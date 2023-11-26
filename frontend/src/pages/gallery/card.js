import React from 'react';
import './card.css';

const ImagWorldCard = ({ imageUrl, title }) => {
  return (
    <div className="image-world-card">
      <img src={imageUrl} alt={title} />
      <div className="card-content">
        <h3>{title}</h3>
      </div>
    </div>
  );
};

export default ImagWorldCard;
