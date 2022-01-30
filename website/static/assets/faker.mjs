import {faker} from "@faker-js/faker";

// const name = faker.name.firstName()
// const userName = faker.internet.userName()
// const email = faker.internet.email()
//
// console.log(name)
// console.log(userName)
// console.log(email)

for (let i = 0; i < 10; i++) {
    const description = faker.commerce.productDescription()
    const productName = faker.commerce.productName()
    const product = faker.commerce.product()
    const barcode = faker.datatype.float()

    console.log('description:  ', description)
    console.log('product   ', product)
    console.log('product name:    ',productName)
    console.log('barcode:    ',barcode)
}
