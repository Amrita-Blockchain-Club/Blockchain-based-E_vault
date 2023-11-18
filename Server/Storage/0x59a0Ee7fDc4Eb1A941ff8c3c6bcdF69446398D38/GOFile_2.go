package main

import (
	"fmt"
	"math/big"

	"github.com/ethereum/go-ethereum/crypto"
)

// ZKPProof represents a zero knowledge proof of knowledge of a preimage
// of a hash function.
type ZKPProof struct {
	// C is a commitment to the preimage.
	C *big.Int
	// V is a vector of values used in the proof.
	V []*big.Int
}

// Verify verifies that the proof is valid for the given hash.
func (p *ZKPProof) Verify(hash *big.Int) bool {
	// Check that the commitment is valid.
	if !crypto.HashToECPoint(hash).Equal(p.C) {
		return false
	}

	// Compute the inner product of the proof vector and the hash.
	innerProduct := big.NewInt(0)
	for i := range p.V {
		innerProduct.Add(innerProduct, p.V[i].Mul(hash, big.NewInt(i+1)))
	}

	// Return true if the inner product is equal to the commitment.
	return innerProduct.Cmp(p.C) == 0
}

// Generate generates a new zero knowledge proof for the given preimage.
func Generate(preimage []byte) (*ZKPProof, error) {
	// Hash the preimage to get a commitment.
	hash := crypto.Keccak256(preimage)
	c := new(big.Int).SetBytes(hash)

	// Generate a random vector of values.
	v := make([]*big.Int, len(preimage))
	for i := range v {
		v[i] = new(big.Int).Rand(rand.Reader)
	}

	// Compute the inner product of the proof vector and the hash.
	innerProduct := big.NewInt(0)
	for i := range v {
		innerProduct.Add(innerProduct, v[i].Mul(hash, big.NewInt(i+1)))
	}

	// Return the proof.
	return &ZKPProof{
		C: c,
		V: v,
	}, nil
}

func main() {
	// Generate a preimage.
	preimage := []byte("Hello, world!")

	// Generate a zero knowledge proof for the preimage.
	proof, err := Generate(preimage)
	if err != nil {
		fmt.Println(err)
		return
	}

	// Verify the proof.
	if !proof.Verify(crypto.Keccak256(preimage)) {
		fmt.Println("Invalid proof")
		return
	}

	// The proof is valid!
	fmt.Println("Valid proof")
}