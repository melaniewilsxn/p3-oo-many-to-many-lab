class Author:
    def __init__(self, name):
        self.name =  name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        total_royalties = 0
        for contract in Contract.all:
            if contract.author == self:
                total_royalties += contract.royalties
        return total_royalties


class Book:
    def __init__(self, title):
        self.title =  title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author) and isinstance(book, Book) and type(date) is str and type(royalties) is int:
            self.author = author
            self.book = book
            self.date = date
            self.royalties = royalties
            type(self).all.append(self)
        else:
            raise TypeError

    @classmethod    
    def contracts_by_date(cls):
        return sorted(cls.all, key=lambda contract: contract.date)