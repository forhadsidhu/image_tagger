import React from 'react';
import { SearchContainer, SearchInput, SearchButton } from './SearchElements';

const SearchField = () => {
  return (
    <SearchContainer>
      <SearchInput type="search" placeholder="Search Anything..." />
      <SearchButton>Search</SearchButton>
    </SearchContainer>
  );
};

export default SearchField;
