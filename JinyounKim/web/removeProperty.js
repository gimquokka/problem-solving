function removeProperty(obj, prop) {
    if (prop in obj){
        delete obj[prop]
        return true
    } else {
        return false
    }
}