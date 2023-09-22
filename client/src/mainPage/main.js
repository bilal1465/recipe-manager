import React, {useState, useEffect} from 'react'
import RecipeTitlesList from './recipeTitlesList'
import AddRecipe from './newRecipe'

function MainPage() {
    
    const [recipeList, editList] = useState({})

    useEffect(() => {
        fetch("/RecipeList").then(
            res => res.json()
        ).then (
            data => {
                editList(data)
            }
        )
        
}, [])
    
    return (
        <div>
            <RecipeTitlesList data={recipeList}/>
            <AddRecipe/>
        </div>
    );

}

export default MainPage